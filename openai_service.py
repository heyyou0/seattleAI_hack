import os, json, time, requests

# API 토큰을 환경 변수에서 가져옵니다.
HF_TOKEN = os.environ.get("HF_API_KEY") or os.environ.get("HF_TOKEN")
HF_MODEL = "HuggingFaceH4/zephyr-7b-beta"
HF_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
HF_HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


def hf_generate(prompt, max_tries=6):
    """Hugging Face Inference API를 호출하고, 일반적인 응답 형식을 처리합니다."""
    # 디버깅을 위해 토큰 상태를 출력합니다.
    if not HF_TOKEN:
        print("HF_TOKEN is not set. API call will fail.")
        return None

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.8,
            "do_sample": True,
            "return_full_text": False
        }
    }
    backoff = 2
    for i in range(max_tries):
        try:
            print(f"Attempting to call HF API (try {i+1})...")
            r = requests.post(HF_URL,
                              headers=HF_HEADERS,
                              json=payload,
                              timeout=60)
        except Exception as e:
            if i == max_tries - 1:
                print(
                    f"Failed to connect to HF API after {max_tries} tries: {e}"
                )
                raise
            print(f"Connection error: {e}. Retrying in {backoff} seconds.")
            time.sleep(backoff)
            backoff *= 1.5
            continue

        # 503: 모델 로딩 중
        if r.status_code == 503:
            try:
                eta = r.json().get("estimated_time", 6)
            except Exception:
                eta = 6
            print(
                f"Model is loading (503). Retrying in {min(eta, 10)} seconds.")
            time.sleep(min(eta, 10))
            continue

        # 200: 응답 성공
        if r.status_code == 200:
            try:
                data = r.json()
                print("HF API call successful.")
            except Exception:
                print("HF API returned non-JSON response. Returning raw text.")
                return r.text.strip()

            if isinstance(data, list) and data:
                gt = data[0].get("generated_text") or data[0].get(
                    "summary_text")
                if gt: return gt.strip()

            if isinstance(data, dict):
                gt = data.get("generated_text") or data.get("text")
                if gt: return gt.strip()

            print(
                f"HF API returned valid JSON but no text content: {json.dumps(data)}"
            )
            return None

        # 404 / 429 / 기타: 나중에 다시 시도
        if r.status_code in (404, 429, 500):
            if i == max_tries - 1:
                print(f"HF error {r.status_code}: {r.text[:200]}")
                return None
            print(
                f"HF API returned {r.status_code}. Retrying in {backoff} seconds."
            )
            time.sleep(backoff)
            backoff *= 1.5
            continue

        # 기타 예상치 못한 상태
        print(
            f"HF API returned unexpected status code {r.status_code}: {r.text[:200]}"
        )
        return None

    print("HF: Model not available, please try again later.")
    return None


def generate_tarot_reading(question, selected_cards, reading_type):
    """
    타로 리딩을 생성합니다. 먼저 Hugging Face API를 시도하고, 실패 시
    미리 정의된 구조화된 리딩을 사용합니다.
    """
    # HF_TOKEN이 설정되어 있다면 API를 호출합니다.
    if HF_TOKEN:
        cards_text = "\n".join(
            f"{c.get('name','Unknown')}: {c.get('description','')}" +
            (f" Keywords: {', '.join(c.get('keywords', []))}" if c.
             get('keywords') else "") for c in selected_cards)
        context = {
            "1-card":
            "This is a single card reading focused on providing direct insight and guidance.",
            "3-card":
            "This is a three-card reading representing Past, Present, and Future influences.",
            "celtic-cross":
            "This is a Celtic Cross reading, a comprehensive 10-card spread that provides deep insight into the situation."
        }.get(reading_type,
              "This is a single card reading focused on guidance.")

        prompt = (
            "You are a wise tarot reader. Write a mystical but concrete reading.\n"
            f"Question: {question}\n\nCards:\n{cards_text}\n\n{context}\n\n"
            "Return only the reading text (no JSON, no explanations).")

        # API를 호출하고 응답을 받습니다.
        text = hf_generate(prompt)

        # API 호출이 성공하고 응답 길이가 충분하면 반환합니다.
        if text and len(text) > 50:
            return text

    # HF API 호출이 실패하거나 토큰이 없는 경우 대체 로직을 실행합니다.
    return generate_structured_reading(question, selected_cards, reading_type)


def generate_structured_reading(question, selected_cards, reading_type):
    """
    Hugging Face API 호출이 실패할 경우를 대비한 대체(fallback) 함수.
    선택된 카드를 기반으로 미리 정해진 형식의 리딩을 생성합니다.
    """
    reading_type_to_title = {
        "1-card": "Your reading for '{}'",
        "3-card":
        "Your three-card reading for '{}' shows the past, present, and future influences:",
        "celtic-cross": "Your Celtic Cross reading for '{}':"
    }

    reading_title = reading_type_to_title.get(
        reading_type, "Your reading for '{}'").format(question)

    reading_parts = [reading_title]

    # 3-card spread에 대한 위치별 제목
    if reading_type == "3-card":
        positions = ["Past", "Present", "Future"]
        for i, card in enumerate(selected_cards):
            card_name = card.get('name', 'Unknown')
            card_description = card.get('description', '')
            keywords = ', '.join(card.get('keywords', []))

            part = (
                f"\n**{positions[i]}: {card_name}**\n"
                f"The {card_name} represents {card_description}.\n"
                f"Key themes: {keywords}\n"
                f"This card suggests: {card_description.split(', ')[0] if card_description else 'No specific suggestions'}"
            )
            reading_parts.append(part)
    else:
        # 다른 스프레드(1-card, celtic-cross 등)에 대한 기본 형식
        for card in selected_cards:
            card_name = card.get('name', 'Unknown')
            card_description = card.get('description', '')
            keywords = ', '.join(card.get('keywords', []))

            part = (
                f"\n**{card_name}**\n"
                f"The {card_name} represents {card_description}.\n"
                f"Key themes: {keywords}\n"
                f"This card suggests: {card_description.split(', ')[0] if card_description else 'No specific suggestions'}"
            )
            reading_parts.append(part)

    reading_parts.append(
        "\n✨ The cards have spoken. Trust your intuition as you move forward on your path."
    )

    return "\n".join(reading_parts)

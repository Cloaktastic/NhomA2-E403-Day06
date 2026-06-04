from __future__ import annotations

import os
from pathlib import Path
from typing import Dict, Iterator, Optional

from openai import OpenAI
from dotenv import load_dotenv

# Points to d:\vinuni\Day06-E403-NhomA2\codebase\.env
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DEFAULT_ENV_PATH = ROOT_DIR / ".env"

def load_env_config(env_path: Path = DEFAULT_ENV_PATH) -> Dict[str, str]:
    load_dotenv(dotenv_path=env_path)

    config = {
        "LLM_ENDPOINT": os.getenv("LLM_ENDPOINT", "").strip(),
        "API_KEY": os.getenv("API_KEY", "").strip(),
        "MODEL": os.getenv("MODEL", "").strip() or "gpt-4o-mini",
    }

    if not config["API_KEY"]:
        raise ValueError("Missing required env value: API_KEY")

    return config


class LLMProvider:
    def __init__(
        self,
        model_name: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        env_path: Path = DEFAULT_ENV_PATH,
    ) -> None:
        config = load_env_config(env_path)

        self.model_name = model_name or config["MODEL"]
        self.api_key = api_key or config["API_KEY"]
        self.base_url = base_url or config["LLM_ENDPOINT"] or None
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
        )
        return response.choices[0].message.content or ""

    def stream(self, prompt: str, system_prompt: Optional[str] = None) -> Iterator[str]:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        stream = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            stream=True,
        )

        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

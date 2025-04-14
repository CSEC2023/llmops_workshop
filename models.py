from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union


class Role(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"


class Provider(str, Enum):
    openai = "openai"
    anthropic = "anthropic"
    groq = "groq"
    ollama = "ollama"


class Message(BaseModel):
    role: Role
    content: str


class ChatCompletionRequest(BaseModel):
    provider: Optional[Provider]
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 256
    stream: Optional[bool] = False


class Choice(BaseModel):
    index: int
    message: Message
    finish_reason: str


class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[Choice]
    usage: Usage
    provider: Provider

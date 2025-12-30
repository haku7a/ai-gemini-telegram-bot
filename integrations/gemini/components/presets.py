from google.genai import types


class GenerationPresets:
    @staticmethod
    def default() -> types.GenerateContentConfig:
        return types.GenerateContentConfig(
            response_modalities=["TEXT"], temperature=0.7
        )

    @staticmethod
    def thinking() -> types.GenerateContentConfig:
        return types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(include_thoughts=False),
            response_modalities=["TEXT"],
        )

    @staticmethod
    def google_search() -> types.GenerateContentConfig:
        return types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())],
            response_modalities=["TEXT"],
        )

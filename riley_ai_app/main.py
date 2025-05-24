import sys
import os
from PyQt6.QtWidgets import QApplication
from gui.interface import RileyMainWindow
from features.knowledge_graph import KnowledgeGraph
from features.code_knowledge import CodeKnowledge

OPENAI_API_KEY = None  # Set your key here or load from config

class RileyApp:
    def __init__(self):
        self.kg = KnowledgeGraph()
        self.code_knowledge = CodeKnowledge(openai_api_key=OPENAI_API_KEY)
        self.riley_name = "riley"

    def process_input(self, user_input):
        text = user_input.strip()
        try:
            # Command parsing for all advanced features
            if text.lower().startswith("!learn "):
                return self.kg.learn_from_text(text[7:])
            elif text.lower().startswith("!wiki "):
                return self.kg.search_wikipedia(text[6:])
            elif text.lower().startswith("!ingest "):
                return self.kg.ingest_file(text[8:])
            elif text.lower().startswith("!recall"):
                query = text[7:] if len(text) > 7 else None
                return self.kg.recall_memory(query)
            elif text.lower().startswith("!code "):
                return self.code_knowledge.answer(text[6:])
            elif text.lower().startswith("!memory"):
                return self.kg.recall_memory()
            elif text.lower().startswith("!selfimprove "):
                return self._feature_response(self.kg.self_improve_reasoning, text[12:])
            elif text.lower().startswith("!swarm "):
                return self._feature_response(self.kg.multi_agent_swarm, text[7:])
            elif text.lower().startswith("!world "):
                return self._feature_response(self.kg.real_time_world_knowledge, text[7:])
            elif text.lower().startswith("!emotion "):
                return self._feature_response(self.kg.emotional_state_modeling, text[9:])
            elif text.lower().startswith("!creative "):
                return self._feature_response(self.kg.creative_synthesis, ["all"], text[10:])
            elif text.lower().startswith("!research "):
                return self._feature_response(self.kg.autonomous_research, text[10:])
            elif text.lower().startswith("!explain "):
                return self._feature_response(self.kg.explainability_engine, text[9:])
            elif text.lower().startswith("!adaptive "):
                return self._feature_response(self.kg.adaptive_personality, "user", text[10:])
            elif text.lower().startswith("!proactive "):
                return self._feature_response(self.kg.proactive_goal_suggestion, text[10:])
            elif text.lower().startswith("!ethics "):
                return self._feature_response(self.kg.ethical_governor, text[8:], context={})
            elif text.lower().startswith("!help"):
                return (
                    "[Riley] Commands:\n"
                    "!learn <text> - Learn from text\n"
                    "!wiki <topic> - Search Wikipedia\n"
                    "!ingest <file_path> - Ingest file into memory\n"
                    "!recall [query] - Recall memory\n"
                    "!code <question> - Coding help\n"
                    "!memory - Show recent memory\n"
                    "!selfimprove <feedback> - Self-improve reasoning\n"
                    "!swarm <task> - Multi-agent swarm\n"
                    "!world <query> - Real-time world knowledge\n"
                    "!emotion <input> - Emotional state modeling\n"
                    "!creative <prompt> - Creative synthesis\n"
                    "!research <goal> - Autonomous research\n"
                    "!explain <decision> - Explainability engine\n"
                    "!adaptive <history> - Adaptive personality\n"
                    "!proactive <context> - Proactive goal suggestion\n"
                    "!ethics <action> - Advanced ethical governor\n"
                    "Just type or address me as 'Riley' for chat."
                )
            # Addressed to Riley or default chat
            if self.riley_name in text.lower():
                # Improved: respond contextually to 'what do you know' and similar
                lowered = text.lower()
                if any(phrase in lowered for phrase in ["what do you know", "what do you no", "what do u know", "what do u no"]):
                    return (
                        "[Riley] I am Riley, your advanced AI assistant. I have access to a wide range of knowledge: "
                        "science, technology, coding, invention, history, and more. You can ask me about programming, "
                        "science, inventions, or even personal advice. Try commands like !help, !wiki <topic>, or just ask me anything!"
                    )
                elif "code" in lowered or "python" in lowered or "how do i" in lowered:
                    return self.code_knowledge.answer(text)
                else:
                    result = self.kg.interpret(text, context={})
                    return result if result else "[Riley] I'm here! How can I help you?"
            # If not addressed to Riley, treat as chat
            else:
                # Default: treat as chat, pass to knowledge graph for interpretation
                result = self.kg.interpret(text, context={})
                return result if result else "[Riley] I'm here! How can I help you?"
        except Exception as e:
            return f"[Riley] Sorry, an error occurred: {e}"

    def _feature_response(self, func, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None:
                return "[Riley] This advanced feature is not yet implemented, but the interface is ready for future upgrades."
            return result
        except Exception as e:
            return f"[Riley] Feature error: {e}"

    def ingest_full_conversation_dataset(self):
        """Ingest the full conversations_full.txt dataset into Riley's memory at startup."""
        dataset_path = os.path.join(os.path.dirname(__file__), 'conversations_full.txt')
        if os.path.exists(dataset_path):
            result = self.kg.ingest_conversation_dataset(dataset_path)
            print(result)
        else:
            print(f"[Riley] conversations_full.txt not found at {dataset_path}")


def main():
    app = QApplication(sys.argv)
    window = RileyMainWindow()
    window.show()
    riley = RileyApp()
    riley.ingest_full_conversation_dataset()  # Ingest full dataset at startup
    def on_user_input(text):
        response = riley.process_input(text)
        window.append_chat(f"You: {text}")
        window.append_chat(response)
    window.on_user_input = on_user_input
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
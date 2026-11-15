#!/usr/bin/env python3
"""
customer-support-agent -- FAQ chatbot for a small shop (rule-based).

No API key needed. Answers are matched to built-in FAQ intents by keywords.
Unknown questions get a polite fallback instead of a made-up answer.

Usage:
    python agent.py --demo        # answer sample questions
    python agent.py               # interactive chat (type 'quit' to exit)
"""

import argparse
import re
import sys

SHOP_NAME = "SliceHouse Pizza"

# intent -> (keywords, answer)
INTENTS = {
    "opening hours": (
        ["open", "hours", "timing", "time", "close", "closing", "when are you open"],
        f"{SHOP_NAME} is open every day from 11:00 AM to 11:00 PM.",
    ),
    "delivery": (
        ["deliver", "delivery", "deliveries", "shipping", "ship", "how long"],
        "We deliver within the city in 30-45 minutes. Delivery is free on orders over Rs. 1,000.",
    ),
    "returns / refund": (
        ["return", "refund", "exchange", "wrong order", "damaged", "cancel"],
        "If your order arrived wrong or damaged, contact us within 24 hours and we will "
        "replace it or refund you. Please keep your order number ready.",
    ),
    "price": (
        ["price", "cost", "how much", "menu", "rates", "cheap", "expensive"],
        "Our pizzas start at Rs. 499 (small), Rs. 799 (medium) and Rs. 1,099 (large). "
        "Ask me about today's deals!",
    ),
    "order status": (
        ["order status", "where is my order", "track", "status of my order", "my order"],
        "To check your order status, please share your order number. "
        "For example, order #12345 is currently out for delivery.",
    ),
    "contact human": (
        ["human", "agent", "person", "representative", "call", "phone", "contact", "talk to someone"],
        "You can reach our support team at 0300-1234567 (11 AM - 11 PM) or email "
        "support@slicehouse.example. A human agent will help you.",
    ),
}

FALLBACK = (
    "I'm sorry, I don't have an answer for that yet. I can help with opening hours, "
    "delivery, returns/refunds, prices, order status, or connecting you to a human agent. "
    "Could you please rephrase your question?"
)

DEMO_QUESTIONS = [
    "What are your opening hours?",
    "How much does a large pizza cost?",
    "Do you deliver to my area?",
    "I want to return my order, what is the refund policy?",
    "Where is my order?",
    "Can I talk to a human?",
    "Do you sell burgers?",  # unknown -> fallback
]


def match_intent(text):
    """Return (intent_name, answer) for the best keyword match, or (None, FALLBACK)."""
    text = text.lower()
    best_intent, best_answer, best_score = None, FALLBACK, 0
    for intent, (keywords, answer) in INTENTS.items():
        score = sum(1 for kw in keywords if kw in text)
        # A multi-word phrase match counts double (more specific).
        score += sum(1 for kw in keywords if " " in kw and kw in text)
        if score > best_score:
            best_intent, best_answer, best_score = intent, answer, score
    return best_intent, best_answer


def answer(question):
    """Answer one question and return (intent, answer)."""
    # Demo order-number handling: "#12345" style order numbers get a status line.
    m = re.search(r"#?\d{4,}", question)
    intent, reply = match_intent(question)
    if intent == "order status" and m:
        reply = f"Order {m.group(0)} is out for delivery and should arrive within 20 minutes."
    return intent, reply


def main():
    parser = argparse.ArgumentParser(description="FAQ chatbot for a small shop (rule-based, no API key).")
    parser.add_argument("--demo", action="store_true", help="Answer built-in sample questions.")
    args = parser.parse_args()

    print(f"Welcome to {SHOP_NAME} support! (Rule-based demo bot - no API key needed.)")
    print("I can help with: opening hours, delivery, returns/refund, price, order status, contact human.")
    print()

    if args.demo:
        for q in DEMO_QUESTIONS:
            intent, reply = answer(q)
            print(f"You: {q}")
            print(f"Bot [{intent or 'fallback'}]: {reply}")
            print()
        return 0

    print("Type your question (or 'quit' / 'exit' to stop).")
    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Thank you for chatting with us. Goodbye!")
            return 0
        if question.lower() in ("quit", "exit", "bye"):
            print("Bot: Thank you for chatting with us. Goodbye!")
            return 0
        if not question:
            continue
        intent, reply = answer(question)
        print(f"Bot [{intent or 'fallback'}]: {reply}")


if __name__ == "__main__":
    sys.exit(main())

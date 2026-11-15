# Customer Support Agent

**Author:** Wajahat Irfan, BS Computer Science student (7th semester), GPGC No. 1 Abbottabad

## What it does
A rule-based FAQ chatbot for a small shop (demo shop: SliceHouse Pizza).
It matches a customer's question to a built-in FAQ intent using keywords and
replies with the matching answer. It never invents answers — unknown
questions get a polite fallback that lists what it can help with.

Built-in intents: opening hours, delivery, returns/refund, price, order
status, contact human.

## How to run
```bash
cd customer-support-agent
python agent.py --demo        # answer sample questions
python agent.py               # interactive chat (type 'quit' to exit)
```

## Example output
```
You: What are your opening hours?
Bot [opening hours]: SliceHouse Pizza is open every day from 11:00 AM to 11:00 PM.

You: Do you sell burgers?
Bot [fallback]: I'm sorry, I don't have an answer for that yet. I can help with
opening hours, delivery, returns/refund, prices, order status, or connecting
you to a human agent. Could you please rephrase your question?
```

## Skills shown
- Python, `argparse` CLI design
- Keyword-based intent matching and scoring
- Graceful fallback handling for unknown input
- Interactive command-line chatbot loop

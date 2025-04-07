
# 🇩🇪 German Sentiment LLM

Ein einfaches Python-Tool zur **Sentimentanalyse deutscher Texte** mithilfe eines vortrainierten BERT-Modells von HuggingFace.

Dieses Projekt verwendet ein LLM (Large Language Model), um Texte auf **positiv**, **neutral** oder **negativ** zu klassifizieren.

---

## 🚀 Beispiel-Nutzung

```bash
> Ich liebe dieses Produkt!
Analyse: [{'label': 'positive', 'score': 0.987...}]
```

```bash
> Ich finde den Kundenservice schrecklich.
Analyse: [{'label': 'negative', 'score': 0.991...}]
```

```bash
> Das Gerät funktioniert.
Analyse: [{'label': 'neutral', 'score': 0.84...}]
```

---

## 🧠 Verwendete Technologien

- [HuggingFace Transformers](https://huggingface.co/transformers/)
- Python 3.10+
- Vortrainiertes Modell: [`oliverguhr/german-sentiment-bert`](https://huggingface.co/oliverguhr/german-sentiment-bert)

---

## 🛠 Installation

1. Repository klonen:

```bash
git clone https://github.com/00fernweh/german-sentiment-llm.git
cd german-sentiment-llm
```

2. Virtuelle Umgebung erstellen und aktivieren:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
```

3. Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ausführen

```bash
python main.py
```

Dann gib einen Satz auf Deutsch ein und erhalte die Stimmungsanalyse.

---

## 📂 Projektstruktur

```
german_sentiment_llm/
├── main.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz veröffentlicht.

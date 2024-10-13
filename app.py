from flask import Flask, render_template, request
from indic_transliteration import sanscript

app = Flask(__name__)

def transliterate_to_devanagari(input_text, source_language):
    # Mapping of source languages to their corresponding scripts
    language_script_map = {
        'hindi': sanscript.DEVANAGARI,
        'bengali': sanscript.BENGALI,
        'gujarati': sanscript.GUJARATI,
        'kannada': sanscript.KANNADA,
        'malayalam': sanscript.MALAYALAM,
        'odisha': sanscript.ORIYA,
        'punjabi': sanscript.GURMUKHI,
        'tamil': sanscript.TAMIL,
        'telugu': sanscript.TELUGU,
        'gunjala gondi': sanscript.GUNJALA_GONDI,
        'grantha': sanscript.GRANTHA,
    }

    # Normalize the source language input
    source_language = source_language.lower()

    # Check if the language is supported
    if source_language not in language_script_map:
        return "Unsupported language."

    # Get the corresponding script
    source_script = language_script_map[source_language]

    # Transliterate to Devanagari
    transliterated_text = sanscript.transliterate(input_text, source_script, sanscript.DEVANAGARI)
    return transliterated_text

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_text = request.form['input_text']
        source_language = request.form['source_language']
        result = transliterate_to_devanagari(input_text, source_language)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)

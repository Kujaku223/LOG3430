import random
import string

class MyFuzzer:

    def __init__(self):
        self.supported_languages = [
            'am', 'ar', 'az', 'by', 'cz', 'en', 'en_IN', 'en_NG', 'fa', 'fr',
            'fr_CH', 'fr_BE', 'fr_DZ', 'de', 'fi', 'eo', 'es', 'es_CO', 'es_GT',
            'es_NI', 'es_VE', 'id', 'ja', 'kn', 'ko', 'kz', 'lt', 'lv', 'pl',
            'ro', 'ru', 'sk', 'sl', 'sr', 'sv', 'no', 'dk', 'pt', 'pt_BR', 'he',
            'it', 'vi', 'tg', 'th', 'tr', 'nl', 'uk', 'te', 'hu', 'is'
        ]
        self.conversion_types = ['cardinal', 'ordinal', 'ordinal_num', 'year', 'currency']

    # Fonction pour générer des nombres aléatoires
    def generate_random_number(self):
        types = [
            random.randint(-1_000_000, 1_000_000),  # entier aléatoire
            random.uniform(-1_000_000.0, 1_000_000.0),  # nombre flottant aléatoire
            "".join(random.choices(string.digits, k=random.randint(1, 10))),  # nombre sous forme de chaîne
        ]
        return random.choice(types)

    def fuzz(self):
        lang = random.choice(self.supported_languages)
        number = self.generate_random_number()
        to_type = random.choice(self.conversion_types)
        random_bool = random.choice([True, False])

        return (number, random_bool, lang, to_type)
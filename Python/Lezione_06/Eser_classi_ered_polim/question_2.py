'''
Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
'''



class RecipeManager:

    def __init__(self):
        self.recipes: dict[str, list[str]] = {}

    def create_recipe(self, name: str, ingredients: list[str]) -> dict[str, list[str]]:
        if name not in self.recipes:
            self.recipes[name] = ingredients
            return self.recipes
        else:
            print('la ricetta esiste già')

    def add_ingredient(self, recipe_name: str, ingredient: str) -> list[str]:
        if recipe_name in self.recipes and ingredient not in self.recipes[recipe_name]:
            self.recipes[recipe_name].append(ingredient)
            return self.recipes[recipe_name]
        else:
            print('errore_add')

    def remove_ingredient(self, recipe_name: str, ingredient: str) -> list[str]:
        if recipe_name in self.recipes and ingredient in self.recipes[recipe_name]:
            self.recipes[recipe_name].remove(ingredient)
            return {recipe_name: self.recipes[recipe_name]}
        else:
            print('errore_remove')

    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> list[str]:
        if recipe_name in self.recipes and old_ingredient in self.recipes[recipe_name]:
            self.recipes[recipe_name].insert(self.recipes[recipe_name].index(old_ingredient), new_ingredient)
            self.recipes[recipe_name].pop(self.recipes[recipe_name].index(old_ingredient))
            return {recipe_name: self.recipes[recipe_name]}
        else:
            print('errore_upd')

    def list_recipes(self) -> dict[str, list[str]]:
        if self.recipes:
            return [recipe for recipe in self.recipes]
    
    def list_ingredients(self, recipe_name: str) -> list[str]:
        if recipe_name in self.recipes:
            return self.recipes[recipe_name]
        else:
            print('errore_list_ingredients')

    def search_recipe_by_ingredient(self, ingredient: str) -> dict[str, list[str]]:
        recipes_by_ingredients: dict[str, list[str]] = {}
        for recipe, ingr in self.recipes.items():
            if ingredient in ingr:
                recipes_by_ingredients[recipe] = self.recipes[recipe]

        if not recipes_by_ingredients:
            print('errore_by')
        else:
            return recipes_by_ingredients
ra = {"Liz": 229874, "Hugo": 215793, "Sofia": 199745}  # Dicionário com nomes como chaves e números de registro como valores

print(ra.get("Hugo"))  # Retorna o valor associado à chave "Hugo" (215793)

print(ra.get("Maria"))  # Retorna None, pois "Maria" não está no dicionário

print(ra.get("Maria", "N/A"))  # Retorna "N/A" caso "Maria" não esteja no dicionário

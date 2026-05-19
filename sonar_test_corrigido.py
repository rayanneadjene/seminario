import os
import logging

# Configuração básica de logging (melhor que print)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CORREÇÃO DE SEGURANÇA: Usar variável de ambiente em vez de senha fixa
# No terminal: export DB_PASSWORD=sua_senha_aqui
DB_PASSWORD = os.getenv("DB_PASSWORD", "default_secure_value")

def calculate_circle_area(radius):
    """Função única para calcular área, evitando duplicação."""
    pi = 3.14159
    return pi * (radius ** 2)

def calculate_area(radius):
    logger.info("Calculating area for radius: %s", radius)
    return calculate_circle_area(radius)

def calculate_volume(radius, height):
    # CORREÇÃO DE DUPLICAÇÃO: Reaproveita o cálculo da área
    logger.info("Calculating volume for radius: %s and height: %s", radius, height)
    area = calculate_circle_area(radius)
    return area * height

# CORREÇÃO DE CODE SMELL: Reduzir número de argumentos (usando dicionário ou objeto)
def function_with_optimized_arguments(params):
    """Recebe um dicionário para evitar excesso de parâmetros."""
    return sum(params.values())

def main():
    # CORREÇÃO: Variável sendo utilizada
    area_result = calculate_area(5)
    logger.info("Area result: %s", area_result)
    
    # CORREÇÃO DE SEGURANÇA: Não imprimir senhas no log/console
    logger.info("Connecting to DB...")

    # CORREÇÃO: Removido 'if True' desnecessário
    logger.info("Process completed successfully")

if __name__ == "__main__":
    main()

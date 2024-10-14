import subprocess
import pkg_resources

# Obter a lista de pacotes instalados
packages = [dist.project_name for dist in pkg_resources.working_set]

# Atualizar cada pacote
for package in packages:
    subprocess.call(f"pip install --upgrade {package}", shell=True)


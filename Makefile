.PHONY: setup data features notebooks clean

# Cria um ambiente virtual e instala as dependências listadas em requirements.txt.
setup:
	python -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "Ambiente pronto. Ative com: source .venv/bin/activate"

# Baixa dados públicos do BCB e, se configurado, do Kaggle.
data:
	. .venv/bin/activate && python scripts/download_data.py

# Gera variáveis derivadas a partir dos dados brutos.
features:
	. .venv/bin/activate && python scripts/build_features.py

# Executa os notebooks de EDA e modelagem usando papermill.
notebooks:
	. .venv/bin/activate && papermill notebooks/01_ews_inadimplencia_eda.ipynb notebooks/01_ews_inadimplencia_eda.out.ipynb
	. .venv/bin/activate && papermill notebooks/02_ews_modelagem.ipynb notebooks/02_ews_modelagem.out.ipynb

# Remove arquivos gerados temporários.
clean:
	rm -f data/processed/*.csv
	rm -f notebooks/*.out.ipynb
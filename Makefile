.PHONY: build validate check serve

build:
	python3 scripts/build_physics_informed_ml_research_package.py --build

validate:
	python3 scripts/build_physics_informed_ml_research_package.py --validate

check:
	python3 -m py_compile scripts/build_physics_informed_ml_research_package.py
	python3 scripts/build_physics_informed_ml_research_package.py --build --validate

serve:
	python3 -m http.server 8022 --directory site


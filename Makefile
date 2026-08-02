.PHONY: build validate check serve remote-check review audit

build:
	python3 scripts/build_physics_informed_ml_research_package.py --build

validate:
	python3 scripts/build_physics_informed_ml_research_package.py --validate

check:
	python3 -m py_compile scripts/build_physics_informed_ml_research_package.py
	python3 -m py_compile scripts/validate_generated_site.py
	python3 -m py_compile scripts/verify_remote_state.py
	python3 scripts/build_physics_informed_ml_research_package.py --build --validate
	python3 scripts/validate_generated_site.py

serve:
	python3 -m http.server 8022 --directory site

remote-check:
	python3 scripts/verify_remote_state.py

review:
	@printf '%s\n' \
		'http://127.0.0.1:8022/handoff.html' \
		'http://127.0.0.1:8022/hand-polish.html' \
		'http://127.0.0.1:8022/meaty-goal-coverage.html' \
		'http://127.0.0.1:8022/review-queue.html' \
		'http://127.0.0.1:8022/evidence-packets.html' \
		'http://127.0.0.1:8022/concept-atlas.html'

audit: check remote-check

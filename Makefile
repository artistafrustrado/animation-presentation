
setup:
	mkdir -p animations
	mkdir -p assets
	mkdir -p blender
	mkdir -p images
	mkdir -p source
	mkdir -p svg
	mkdir -p videos

test:
#	python -m py_compile xxxxx.py
	python -m py_compile blender/scripts/AnimationBuilder.py 
	python -m py_compile blender/scripts/JsonCreate.py


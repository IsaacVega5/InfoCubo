from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ['ttkbootstrap'], 'excludes': [], 'include_files':['assets/', 'README.md'] }

base = 'gui'

executables = [
    Executable('main.py', base=base, target_name = 'InfoCubo', icon='assets/cube.ico')
]

setup(name='InfoCubo',
      version = '1.0',
      author='Isaac Vega Salgado',
      author_email='isaacvega361@gmail.com',
      description = 'Pequeño programa para calcular indices de imágenes hiperespectrales',
      options = {'build_exe': build_options},
      executables = executables)

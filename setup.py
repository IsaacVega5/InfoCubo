from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ['ttkbootstrap', 'numpy'], 'excludes': [], 'include_files':['assets/', 'README.md'] }

base = 'gui'

executables = [
    Executable('main.py', base=base, target_name = 'InfoCubo', icon='assets/cube.ico')
]

setup(name='InfoCubo',
      version = '2.0',
      author='Isaac Vega Salgado',
      author_email='isaacvega361@gmail.com',
      description = 'InfoCubo',
      options = {'build_exe': build_options},
      executables = executables)

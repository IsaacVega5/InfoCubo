def get_name_from_path(path):
  name = path.split("/")[-1]
  name = name.split(".")[0]
  return name

def get_full_name_from_path(path):
  name = path.split("/")[-1]
  return name

def remove_name_from_path(path):
  name = get_full_name_from_path(path)
  new_path = path.replace(name, "")
  return new_path
# import json
# with open('keys.json') as f:
#     data = json.load(f)
#     keys = list(data.keys())

# for ke in keys:
#     if "bearer" in ke:
#         print(f"{ke}:{data[ke]}")
        
# mass = []

# for ke in keys:
#     if "bearer" in ke:
#         mass.append(data[ke])

# print(mass)

# def get_bearer_from_json():
#     bearer_list = []
#     with open ("keys.json") as file:
#         data = json.load(file)
#         keys = list(data.keys())
#     for k in keys:
#         if "bearer" in k:
#             bearer_list.append(data[k])
#     return bearer_list

# bearer_list = get_bearer_from_json()
# print(len(bearer_list))
# for x in range(len(bearer_list)):
#     bearer_token = str(bearer_list[x])
#     print(bearer_token)


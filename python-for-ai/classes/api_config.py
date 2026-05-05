class APIConfig:
    # class attributes - shared by ALL APIConfig instances
    version = 1.0
    max_retries = 3

    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        # instance attributes - unique to each instance of APIConfig
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens

dev_config = APIConfig("sk-dev-key", max_tokens=50)
prod_config = APIConfig("sk-prod-key", model="gpt-4", max_tokens=1000)

print(dev_config.model)
print(prod_config.model)
print(prod_config.max_tokens)
print(dev_config.version)

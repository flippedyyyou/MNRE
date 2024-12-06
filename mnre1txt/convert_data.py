import json
# transform_data.py

from relation_classes import relation_classes

def build_sentence(tokens):
    """Combine tokens into a full sentence with appropriate spacing."""
    return " ".join(tokens).replace(" :", ":")

def get_relation_data(relation_key):
    """Extract the class definition, description, and examples for a given relation key."""
    relation_data = relation_classes.get(relation_key)
    if relation_data:
        description_start = relation_data.find("Description:")
        examples_start = relation_data.find("Examples:")
        description = relation_data[description_start:examples_start].strip()
        examples = relation_data[examples_start:].strip()
        return {"description": description, "examples": examples}
    return None

def transform_data(original_data):
    """Transform the original data into the desired format."""
    sentence = build_sentence(original_data["token"])
    relation_key = original_data["relation"].split("/")[-1]  # Extract relation type like 'part_of'
    
    print("Extracted relation key:", relation_key)
    
    #若关系类别为None
    if relation_key == "none":
        prompt = """class Entity:
        \"\"\"
        The base class for all entities.
        \"\"\"
        def __init__(self, name: str):
            self.name = name

    class Relation:
        \"\"\"
        The base class for all relations.
        \"\"\"
        def __init__(self, head_entity: Entity, tail_entity: Entity):
            self.head_entity = head_entity
            self.tail_entity = tail_entity
    """
        output = f"""results = []"""
        # Build final transformed data
        transformed_data = {
            "img_id": original_data["img_id"],  
            "sentence": sentence,
            "one-stage": {
                "zero-shot": {
                    "prompt": prompt,
                    "output": output,
                    "prompt_tokenized_length": len(prompt)
                }
            },
            "two-stage": {},
            "relations": []
        }
        return transformed_data
        
    # Get relation class, description, and examples
    prompt = f"""class Entity:
    \"\"\"
    The base class for all entities.
    \"\"\"
    def __init__(self, name: str):
        self.name = name

class Relation:
    \"\"\"
    The base class for all relations.
    \"\"\"
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        self.head_entity = head_entity
        self.tail_entity = tail_entity

{relation_classes[relation_key]}

\"\"\"
This is an object-oriented programming task: instantiate all corresponding Relation Objects in the following sentence.
\"\"\"
sentence = \"{sentence}\""""

    output = f"""results = [
    {relation_key.capitalize()}(Entity("{original_data['h']['name']}"), Entity("{original_data['t']['name']}"))
]"""

    relation_instance_code = f"""{relation_key}_relation1 = {relation_key.capitalize()}(
    head_entity = Entity("{original_data['h']['name']}"),
    tail_entity = Entity("{original_data['t']['name']}")
)"""

    # Build final transformed data
    transformed_data = {
        "img_id": original_data["img_id"],  
        "sentence": sentence,
        "one-stage": {
            "zero-shot": {
                "prompt": prompt,
                "output": output,
                "prompt_tokenized_length": len(prompt)
            }
        },
        "two-stage": {},
        "relations": [
            {
                "type": relation_key.capitalize(),
                "head": {
                    "name": original_data["h"]["name"],
                    "type": "Entity",
                    "pos": original_data["h"]["pos"]
                },
                "tail": {
                    "name": original_data["t"]["name"],
                    "type": "Entity",
                    "pos": original_data["t"]["pos"]
                },
                "code": relation_instance_code,
                "type_id": "Unknown"
            }
        ]
    }
    return transformed_data

# Function to process input JSONL and output formatted JSONL
def process_jsonl(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            data = json.loads(line)
            output_data = transform_data(data)

            # Write the output data to the JSONL file
            outfile.write(json.dumps(output_data) + '\n')



# Example usage
input_file = "/home/shenruoyan/experiments/MNRE/mnre1txt/ours_val.txt"
temp_file = "/home/shenruoyan/experiments/MNRE/mnre1txt/mnre1_val.jsonl"
output_file = "/home/shenruoyan/experiments/MNRE/mnre1txt/mnre1_formatted_val.jsonl"

# 打开txt文件和jsonl输出文件
with open(input_file, 'r', encoding='utf-8') as infile, open(temp_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        # 去除空格和换行符
        line = line.strip()
        
        if line:  # 如果行不为空
            # 解析字典字符串为Python字典
            data = eval(line)  # 使用eval将字符串转为字典，这里假设输入是正确的字典格式
            # 写入jsonl文件
            json.dump(data, outfile)
            outfile.write('\n')

process_jsonl(temp_file, output_file)

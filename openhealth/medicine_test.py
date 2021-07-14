import os
import openai


import requests

api_key = os.getenv("OPENAI_API_KEY")


fileList = openai.File.list()

print(fileList)

#response = openai.File.create(
#  file=open("medicine.jsonl"),
#  purpose='search'
#)

#print(response)


#openai.File.retrieve("file-T339XXWULprZ7R0e9vxXjs57")

#openai.File("file-T339XXWULprZ7R0e9vxXjs57").delete()
#openai.Answer.create(
#    search_model="ada", 
#    model="curie", 
#    question="what is riple A syndrome?", 
#    file="file-GclVOXmTbzyevQ2nNWsN40Ao",
#    examples_context="Triple A syndrome is a very rare multisystem disease characterized by adrenal insufficiency with isolated glucocorticoid deficiency, achalasia, alacrima, autonomic dysfunction and neurodegeneration",
#   examples=[["what is AADC deficiency?","A rare, severe, genetic neurometabolic disorder associated with clinical manifestations related to impaired synthesis of dopamine, noradrenaline, adrenaline and serotonin. Clinical manifestations are typically characterized by early-onset muscular hypotonia, movement disorders , developmental delay, ptosis and non-motor symptoms."]], 
#    max_rerank=10,
#    max_tokens=5,
#    stop=["\n", "<|endoftext|>"]
#)

search_response = openai.Engine("davinci").search(
    search_model="davinci", 
    query="AAE2", 
    max_rerank=5,
    file="file-W0lRaPkO3X9FlWZM4jxLaYms",
    return_metadata=True
)

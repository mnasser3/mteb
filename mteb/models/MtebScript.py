import mteb
model_name = "sentence-transformers/gtr-t5-xxl"
model = mteb.get_model(model_name) 
tasks = mteb.get_benchmark("MTEB(eng, classic)")
evaluation = mteb.MTEB(tasks=tasks)
results = evaluation.run(model, output_folder=f"results/{model_name}")
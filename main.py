import pandas as pd
from pycaret.regression import *

data = pd.read_csv("./data/student_data.csv")
df = data.copy()

setup(data=df, target="G3", session_id=42)

best_model = compare_models()
tuned_ada = tune_model(best_model)
tuned_xgb = tune_model(create_model('xgboost'))
tuned_rf  = tune_model(create_model('rf'))

best_final = compare_models(include=[tuned_ada, tuned_xgb, tuned_rf])

final_model = finalize_model(best_final)

plot_model(best_final, plot='feature', save=True)
interpret_model(tuned_xgb, save=True)

save_model(final_model, 'student_model')
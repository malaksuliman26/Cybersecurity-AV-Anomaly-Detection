# My Cybersecurity System for Vehicle Sensors in Palestine
# Student: malak

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

print("="*50)
print("MY CYBERSECURITY SYSTEM FOR VEHICLE SENSORS")
print("="*50)

# Step 1: Load dataset
print("\n[1] Loading NSL-KDD dataset...")
column_names = ['duration','protocol_type','service','flag','src_bytes','dst_bytes',
                'land','wrong_fragment','urgent','hot','num_failed_logins','logged_in',
                'num_compromised','root_shell','su_attempted','num_root','num_file_creations',
                'num_shells','num_access_files','num_outbound_cmds','is_host_login',
                'is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
                'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
                'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
                'dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate',
                'dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
                'dst_host_rerror_rate','dst_host_srv_rerror_rate','label','difficulty']

df = pd.read_csv('KDDTrain+.txt', names=column_names)
print(f"   Loaded {len(df)} samples")

# Step 2: Preprocess data
print("\n[2] Preprocessing data...")
categorical_cols = ['protocol_type', 'service', 'flag']
for col in categorical_cols:
    df[col] = LabelEncoder().fit_transform(df[col])

df['target'] = np.where(df['label'] == 'normal', 0, 1)
X = df.drop(['label', 'target'], axis=1)
y = df['target']
X_scaled = StandardScaler().fit_transform(X)
print("   Preprocessing complete")

# Step 3: Split data (train on normal only)
print("\n[3] Splitting data...")
X_train = X_scaled[y == 0]
X_test = X_scaled
y_test = y
print(f"   Training samples (normal only): {len(X_train)}")
print(f"   Testing samples: {len(X_test)}")

# Step 4: Train Isolation Forest
print("\n[4] Training Isolation Forest model...")
model = IsolationForest(n_estimators=100, contamination=0.25, random_state=42)
model.fit(X_train)
print("   Training complete")

# Step 5: Make predictions
print("\n[5] Making predictions...")
predictions = model.predict(X_test)
predictions = [1 if x == -1 else 0 for x in predictions]

# Step 6: Display results
print("\n[6] Results:")
print(f"   Accuracy:  {accuracy_score(y_test, predictions)*100:.1f}%")
print(f"   Precision: {precision_score(y_test, predictions)*100:.1f}%")
print(f"   Recall:    {recall_score(y_test, predictions)*100:.1f}%")
print(f"   F1-Score:  {f1_score(y_test, predictions)*100:.1f}%")

print("\n[7] Confusion Matrix:")
cm = confusion_matrix(y_test, predictions)
print("                 Predicted")
print("              Normal   Attack")
print(f"Actual Normal    {cm[0,0]}      {cm[0,1]}")
print(f"       Attack    {cm[1,0]}      {cm[1,1]}")

print("\n" + "="*50)
print("SYSTEM EXECUTION COMPLETE")
print("="*50)
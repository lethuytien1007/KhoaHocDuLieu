# Import các thư viện cần thiết
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# ==========================================
# BƯỚC 1: TẢI VÀ ĐỌC DỮ LIỆU
# ==========================================
# Thay đổi đường dẫn này nếu file CSV của bạn nằm ở thư mục khác
file_path = r"C:\Users\Asus\Downloads\Financial Statement Anomaly Dataset.csv"
df = pd.read_csv(file_path)

# ==========================================
# BƯỚC 2: KHÁM PHÁ DỮ LIỆU (EDA)
# ==========================================
print("=== 1. THÔNG TIN TỔNG QUAN DỮ LIỆU ===")
print(df.info())

print("\n=== 2. PHÂN PHỐI NHÃN (TÌNH TRẠNG TÀI CHÍNH) ===")
print(df['Financial_Status'].value_counts())

# ==========================================
# BƯỚC 3: TIỀN XỬ LÝ DỮ LIỆU
# ==========================================
# Tách dữ liệu thành 2 phần: X (Đề bài/Chỉ số) và y (Đáp án/Nhãn)
X = df.drop(columns=['Financial_Status'])
y = df['Financial_Status']

# Chia dữ liệu: 80% để máy học (Train), 20% để kiểm tra (Test)
# Tham số stratify=y giúp giữ nguyên tỷ lệ Bình thường/Rủi ro ở cả 2 tập
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ==========================================
# BƯỚC 4: HUẤN LUYỆN MÔ HÌNH (MACHINE LEARNING)
# ==========================================
print("\n=== 3. ĐANG HUẤN LUYỆN MÔ HÌNH... ===")
# Khởi tạo thuật toán Random Forest
# class_weight='balanced' ép máy tính phải học kỹ các nhóm thiểu số (Anomaly, High Risk)
model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)

# Bắt đầu cho máy học
model.fit(X_train, y_train)
print("Huấn luyện thành công!")

# ==========================================
# BƯỚC 5: DỰ ĐOÁN VÀ ĐÁNH GIÁ KẾT QUẢ
# ==========================================
# Cho máy làm bài kiểm tra trên tập dữ liệu Test (20% đã tách ra ở trên)
y_pred = model.predict(X_test)

print("\n=== 4. BÁO CÁO KẾT QUẢ DỰ ĐOÁN (CLASSIFICATION REPORT) ===")
# In ra báo cáo chi tiết về độ chính xác (Precision, Recall, F1-Score)
print(classification_report(y_test, y_pred, zero_division=0))

# ==========================================
# BƯỚC 6: TRỰC QUAN HÓA (VẼ BIỂU ĐỒ)
# ==========================================
# Vẽ Ma trận nhầm lẫn (Confusion Matrix) để xem máy đoán sai ở đâu
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)

# Dùng thư viện Seaborn để vẽ biểu đồ nhiệt (Heatmap) cho đẹp mắt
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=model.classes_,
            yticklabels=model.classes_)

plt.title('Ma trận nhầm lẫn (Confusion Matrix)')
plt.xlabel('Kết quả Máy dự đoán (Predicted)')
plt.ylabel('Kết quả Thực tế (Actual)')
plt.show()
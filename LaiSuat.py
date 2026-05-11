def tinh_loi_nhuan(so_tien_ban_dau, lai_suat_thang_phan_tram, so_thang=12):
    # Đổi phần trăm thành số thập phân (VD: 0.5% = 0.005)
    lai_suat = lai_suat_thang_phan_tram / 100
    
    # Công thức tính lãi kép: Tổng tiền = Tiền gốc * (1 + lãi suất)^số tháng
    tong_tien_cuoi_ky = so_tien_ban_dau * ((1 + lai_suat) ** so_thang)
    loi_nhuan = tong_tien_cuoi_ky - so_tien_ban_dau
    
    return loi_nhuan, tong_tien_cuoi_ky

# Chạy thử chương trình
von_ban_dau = int(input("Nhap so von ban dau: "))
lai_suat_moi_thang = 0.5  # 0.5% / tháng

loi_nhuan, tong_thu = tinh_loi_nhuan(von_ban_dau, lai_suat_moi_thang)

# Sử dụng định dạng :,.0f để in số tiền có dấu phẩy ngăn cách hàng nghìn
print(f"Số tiền gốc: {von_ban_dau:,.0f} VNĐ")
print(f"Lợi nhuận sau 12 tháng: {loi_nhuan:,.0f} VNĐ")
print(f"Tổng tiền thu về: {tong_thu:,.0f} VNĐ")
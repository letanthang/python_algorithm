import tensorly as tl
from tensorly.decomposition import parafac
import numpy as np

# Tạo một tensor ngẫu nhiên 3 chiều
tensor = tl.tensor(np.random.random((4, 3, 2)))

# Thực hiện Parafac decomposition
factors = parafac(tensor, rank=2)

# Kết quả là một list chứa 3 ma trận yếu tố
A, B, C = factors.factors

# In các ma trận yếu tố
print("Matrix A (size {}):".format(A.shape))
print(A)

print("Matrix B (size {}):".format(B.shape))
print(B)

print("Matrix C (size {}):".format(C.shape))
print(C)

# Khôi phục lại tensor từ các yếu tố
reconstructed_tensor = tl.cp_to_tensor(factors)

# In tensor gốc và xấp xỉ
print("Original tensor:")
print(tensor)

print("Reconstructed tensor (approximation):")
print(reconstructed_tensor)

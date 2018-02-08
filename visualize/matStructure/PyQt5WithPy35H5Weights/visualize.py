import h5py
import matplotlib.pyplot as plt

with h5py.File('/med_data/ImageSimilarity/Databases/MRPhysics/CNN/Headcross/4848/correction/normal4848.h5', 'r') as hf:
	train_ref = hf['train_ref'][:]
	train_art = hf['train_art'][:]

nPatch = train_ref.shape[0]

for i in range(nPatch // 6):
	fig, axes = plt.subplots(nrows=5, ncols=2)
	plt.gray()

	cols_title = ['train_ref', 'train_art']

	for ax, col in zip(axes[0], cols_title):
		ax.set_title(col)

	for j in range(5):
		axes[j, 0].imshow(train_ref[6 * i + j])
		axes[j, 1].imshow(train_art[6 * i + j])

	plt.show()
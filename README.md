ViT based ECG image classifier.



Take frequency domain into account by combining additional channels to the background removed ECG image data.

Each channels are image of merged patchs, and each patchs are 1D FFT(by row) of k adjecent(in row) ViT patchs.

![1](https://github.com/user-attachments/assets/2e190f60-1dd2-4da4-b450-8ea154282f6e)
![2](https://github.com/user-attachments/assets/9e80bb9d-920a-4797-be61-9f35f2702aff)



This idea is based on the fact that one can find more noisy 1D FFT patchs in ECG with AF, which is irregularly irregular, while ECG without AF shows certain lines corresponding to heartbeat frequency.



But failed to train this model...

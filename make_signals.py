import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from scipy.interpolate import interp1d
n = 1024
sr = 0.004
data = []

x = np.ones(n).cumsum()-1
for i in range(20):
    data.append(np.random.normal(0, 0.3, size=n).cumsum())

data = np.array(data)
print(data.shape)

t = np.linspace(-.1, .1, .2//sr, endpoint=False)
print(t.shape)
wavelet = sig.gausspulse(t, fc=30, bw=1)

# plt.figure()
# for i in range(len(data)):
#     plt.plot( data[i]+i,x)
# plt.gca().invert_yaxis()
# plt.grid()
# plt.show()

vmin = 1500

thicknesses = np.random.randint(10,500,100)
# thicknesses = np.array([1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000])
vels = np.random.randint(100,500,len(thicknesses)) + np.linspace(1500,2500,len(thicknesses))
tseis = np.linspace(0,4,int(4/sr+1))

times = [0,*(np.cumsum(thicknesses/vels).tolist()[:-1])]
times=np.array(times)
v = np.interp(tseis, times,vels)
f = interp1d(times,vels, kind='previous')
v = f(tseis)
print('Total time={:.3f}s'.format(np.sum(times)))


seis = np.convolve(np.diff(v), wavelet, mode='valid')/10

shift = len(wavelet)
print(seis.shape, tseis.shape)

fig, axes = plt.subplots(1,2, figsize=(12,8))
axes[0].step(v, tseis, lw=.25)
spacing=20
for i in range(10):
    axes[1].plot(seis+i*spacing, tseis[:len(seis)]+shift*sr/2, 'k-',lw=.5, )
# plt.fill(seis,tseis[:len(seis)]+shift*sr/2, lw=.2)

axes[0].invert_yaxis()
axes[1].invert_yaxis()
axes[1].grid()
plt.show()

# plt.plot(t, wavelet, )
# plt.show()



def plot_features(data, data_features, Fs=None, channels=None,first_point=0, last_point=100, num_chan=None, type_feature=None):
# ?--------------------------- Check type, dimensional data & set channels -------------------------------
    if data.ndim < 3:
        if data.shape[0] < data.shape[1]:
            data = data.T
    if data_features.shape[0] < data_features.shape[1]:
            data_features = data_features.T
     
    if 'DataFrame' not in str(type(data)):     
        data = pd.DataFrame(data)
    if 'DataFrame' not in str(type(data_features)):     
        data_features = pd.DataFrame(data_features)
        
    if channels is not None:
        data.columns=channels 
    else:
        data.columns = np.arange(1,data.shape[1]+1)
    # !-------------------------------------------- Set figure -----------------------------------------------   
    _, axs = plt.subplots(nrows=1, ncols=2, sharey='row', figsize=(10,4))

    data = data.iloc[first_point:last_point,:num_chan]
    data_features = data_features.iloc[first_point:last_point,:num_chan]
    if Fs is not None and np.array(Fs) > 0:
        time = (np.linspace(start=first_point/Fs, stop=last_point/Fs, num=len(data))).flatten()
        axs[0].plot(time, data + 80*np.arange(data.shape[1],0,-1))
        axs[0].set_xlabel('Time (sec)', fontsize=10)
        
        axs[1].plot(time, data_features + 80*np.arange(data_features.shape[1],0,-1))
        axs[1].set_xlabel('Time (sec)', fontsize=10)
    else:
        axs[0].plot(data + 80*np.arange(data.shape[1],0,-1))
        axs[0].set_xlabel('sample', fontsize=10)
        
        axs[1].plot(data_features + 80*np.arange(data_features.shape[1],0,-1))
        axs[1].set_xlabel('sample', fontsize=10)
        
    axs[0].set_ylim([np.min(80*np.arange(data.shape[1],0,-1))+np.min(data.iloc[:,data.shape[1]-1]), np.max(80*np.arange(data.shape[1],0,-1))+np.max(data.iloc[:,0])])
    axs[1].set_ylim([np.min(80*np.arange(data_features.shape[1],0,-1))+np.min(data_features.iloc[:,data_features.shape[1]-1]), np.max(80*np.arange(data_features.shape[1],0,-1))+np.max(data_features.iloc[:,0])])
    
    axs[0].set_yticks((80*np.arange(data.shape[1],0,-1)))
    axs[1].set_yticks((80*np.arange(data_features.shape[1],0,-1)))
    axs[0].set_yticklabels(data.columns[:num_chan])
    axs[0].tick_params(axis='x', labelsize=8)
    axs[1].tick_params(axis='x', labelsize=8)
    axs[0].tick_params(axis='y', labelsize=8)
    axs[0].set_ylabel('Channels', fontsize=10)
    axs[0].set_title('Raw signal', fontsize=10)
    axs[1].set_title(type_feature, fontsize=10)
    axs[0].autoscale(enable=None, axis="y", tight=True)
    axs[1].autoscale(enable=None, axis="y", tight=True)
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.02, hspace=0.0)
    axs[0].tick_params(axis='y', color='k', labelcolor='k')
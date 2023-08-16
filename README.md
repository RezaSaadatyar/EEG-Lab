**EEG Lab**


**Principal Component Analysis (PCA):**<Br/>
PCA aims to capture the most significant variations in the data by finding the linear combinations of the original EEG channels that *maximize variance*. The first principal component explains the most variance, the second explains the second most, and so on.<br/>

*Application of PCA to EEG Signals:*<br/>
 - **Dimensionality Reduction:** PCA can help reduce the dimensionality of the data by selecting a subset of the principal components that retain most of the relevant information.
 - **Noise Reduction:** PCA can help filter out noise and unwanted artifacts in EEG signals by emphasizing the components that contain signal-related information while attenuating those related to noise.
 - **Feature Extraction:** PCA extracts features from the original EEG channels that are relevant for the underlying neural activity. These features can be used for various tasks, such as classification, event detection, or understanding brain dynamics.
 - **Visualization:** PCA can be used to visualize the EEG data in a lower-dimensional space, making it easier to explore patterns and relationships among channels and time samples.
 - **Source Localization:** By applying PCA to the covariance matrix of EEG data, it is possible to identify regions of the brain that contribute most to the observed signal, aiding in source localization.<br/>
  - *Step 1: Data Centering*<br>Subtract the mean of each feature (column) from the data matrix to center it around the origin. $X_{centered}= X- mean(X)$<br>
 - *Step 2: Compute the Covariance Matrix*<br>
Calculate the covariance matrix of the centered data. If X is the centered data matrix with rows as observations and columns as features, the covariance matrix C is given by: $C=X_{centered}X_{centered}^{T}/(n-1)\rightarrow$ Where n is the number of samples.
 - *Step 3: Compute Eigenvectors and Eigenvalues*<br>
Calculate the eigenvectors and eigenvalues of the covariance matrix. Eigenvectors represent the directions (principal components) in which the data varies the most, and eigenvalues indicate the amount of variance along each eigenvector.
$C*V_{i}=E_{i}*V_{i}\rightarrow$  E: eigenvalue and V: eigenvector.<br/>
 - *Step 4: Select Principal Components*<br/>
Sort the eigenvalues in decreasing order. The eigenvectors corresponding to the highest eigenvalues are the principal components that capture the most variance in the data.<br/>
- *Step 5: Project Data onto Principal Components*<br/>
Project the centered data onto the selected principal components to obtain the reduced-dimensional representation. If *P*
is a matrix of the selected principal components, the transformed data *Y* is given by: $Y=X_{centered}.P$

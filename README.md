**EEG Lab**

**Artifacts:**<br/>
![Artifacts](https://github.com/RezaSaadatyar/EEG-Lab/assets/96347878/5b103be3-7a81-4a42-86f5-2a6a5d3fc837)

---
**Principal Component Analysis (PCA) Technique for EEG Signals:**<Br/>
PCA aims to capture the most significant variations in the data by finding the linear combinations of the original EEG channels that *maximize variance*. The first principal component explains the most variance, the second explains the second most, and so on.<br/>
**Application of PCA:**<br/>
 - **Dimensionality Reduction:** PCA can help reduce the dimensionality of the data by selecting a subset of the principal components that retain most of the relevant information.
 - **Noise Reduction:** PCA can help filter out noise and unwanted artifacts in EEG signals by emphasizing the components that contain signal-related information while attenuating those related to noise.
 - **Feature Extraction:** PCA extracts features from the original EEG channels that are relevant for the underlying neural activity. These features can be used for various tasks, such as classification, event detection, or understanding brain dynamics.
 - **Visualization:** PCA can be used to visualize the EEG data in a lower-dimensional space, making it easier to explore patterns and relationships among channels and time samples.
 - **Source Localization:** By applying PCA to the covariance matrix of EEG data, it is possible to identify regions of the brain that contribute most to the observed signal, aiding in source localization.<br/>

**Process:**
  - **Step 1: Data Centering** $\rightarrow$ Subtract the mean of each feature (column) from the data matrix to center it around the origin. $X_{centered}= X- mean(X)$<br/>
  - **Step 2: Compute the Covariance Matrix** $\rightarrow$ Calculate the covariance matrix of the centered data. If X is the centered data matrix with rows as observations and columns as features, the covariance matrix C is given by: $C={1 \over (n-1)}X_{centered}X_{centered}^{T}\rightarrow$ Where n is the number of samples.
  - **Step 3: Compute Eigenvectors and Eigenvalues** $\rightarrow$ Calculate the eigenvectors and eigenvalues of the covariance matrix. Eigenvectors represent the directions (principal components) in which the data varies the most, and eigenvalues indicate the amount of variance along each eigenvector.
$C*V_{i}=E_{i}*V_{i}\rightarrow$  E: eigenvalue and V: eigenvector.<br/>
  - **Step 4: Select Principal Components** $\rightarrow$ Sort the eigenvalues in decreasing order. The eigenvectors corresponding to the highest eigenvalues are the principal components that capture the most variance in the data.<br/>
  - **Step 5: Project Data onto Principal Components** $\rightarrow$ Project the centered data onto the selected principal components to obtain the reduced-dimensional representation. If *P* is a matrix of the selected principal components, the transformed data *Y* is given by: $Y=X_{centered}.P$

----
**Common Average Reference (CAR)Technique for EEG Signals:**<br/>
CAR is a widely used technique in EEG signal processing to mitigate the effects of common noise across multiple electrode channels. It aims to improve the quality of EEG data by removing or reducing common sources of noise, such as the placement of electrodes, cable movement, or external electromagnetic interference or muscle activity. CAR $\rightarrow$ *Improving the signal-to-noise ratio of the EEG data.*<br/> $x_{i}(t)=x_{i}(t)-{1 \over C}\sum_{j=1}x_{j}(t); j=1,...,C$<br/>
**Process:**<br/>
 - **Step 1: Calculating the Average Signal** $\rightarrow$ Calculate the average signal across all electrodes at each time point. This average represents the common noise present in the recording.
 - **Step 2: Subtracting the Average Signal:**  $\rightarrow$ Subtract the calculated average signal from the individual electrode signals. This helps remove the common noise component.<br/>

**Drawbacks:**
 - **Preserving Spatial Information:** While CAR reduces common noise, it can also remove some spatial information, which might be important for analyzing brain dynamics involving localized activity.
 - **Reference Bias:** CAR can introduce a reference bias, where the subtraction of the average signal might also remove part of the true brain signal. This can be problematic in scenarios where accurate amplitude information is crucial.
 - **Electrode Artifacts:** CAR might not completely eliminate the effects of electrode artifacts or certain types of noise that are not truly common across all channels.

----
**Laplacian Technique for EEG Signals:**<br/>
It  is a spatial filtering technique used in EEG signal processing. It aims to enhance spatial resolution by highlighting local changes in EEG signal activity while attenuating more widespread activity. This technique can help improve the detection of localized brain events and reduce the effects of distant sources and common noise. The Laplacian $x_{i}$ for electrode i is calculated as follows:<br/>
$x_{i}(t)=x_{i}(t) - \sum_{j\epsilon N_{i}}w_{ij}{x_{j}}; w_{ij}={1/d_{ij} \over \sum_{j\epsilon N_{i}} 1/d_{ij}}$<br/>
$x_{i}(t)$ is the potential of the electrode i compare to the reference electrode, $ω_{ij}$ is the constant weight, $d_{ij}$ is the Euclidean distance from electrode i to electrode j. $N_{i}$ is the set of neighborhood electrodes of center electrode i.
**Process:**<br/>
  - *Neighborhood Definition:* Determine the set of neighboring electrodes for each electrode. Typically, a set of adjacent electrodes is chosen.
  - *Calculation:* For each electrode, calculate the Small Laplacian by subtracting the average of neighboring electrodes' signals from the signal of interest.
----




**Independent Component Analysis (ICA)**<br/> 
ICA is a method to recover a version, of the sources by multiplying the data by an unmixing matrix, U = WX,<br/> 
X is the data (channels x time)<br/> 
U are the ICA source activities (component x time) W is the ICA unmixing matrix (components x channels)<br/> 
While PCA simply decorrelates the outputs (using an orthogonal matrix W), ICA attempts to make the outputs statistically independent, while placing no constraints on the matrix W.<br/> 

















Independent Component Analysis (ICA): ICA is another technique used for artifact removal and source separation. It can be more sophisticated than CAR in terms of extracting independent sources of noise and brain signals.

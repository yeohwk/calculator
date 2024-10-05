import numpy as np

class KalmanFilter:
    def __init__(self, dt, u, std_acc, x_std_meas, y_std_meas, z_std_meas):
        # Define sampling time
        self.dt = dt

        # Define the 3D state variables (position and velocity)
        self.u = u
        self.x = np.zeros((6, 1))

        # Define the state transition matrix
        self.A = np.array([[1, 0, 0, self.dt, 0, 0],
                           [0, 1, 0, 0, self.dt, 0],
                           [0, 0, 1, 0, 0, self.dt],
                           [0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 0, 1]])

        # Define the control input matrix
        self.B = np.array([[0.5 * self.dt**2, 0, 0],
                           [0, 0.5 * self.dt**2, 0],
                           [0, 0, 0.5 * self.dt**2],
                           [self.dt, 0, 0],
                           [0, self.dt, 0],
                           [0, 0, self.dt]])

        # Define the measurement mapping matrix
        self.H = np.array([[1, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0]])

        # Initial covariance matrix
        self.P = np.eye(6)

        # Define the process noise covariance matrix
        self.Q = std_acc**2 * np.array([[0.25 * self.dt**4, 0, 0, 0.5 * self.dt**3, 0, 0],
                                        [0, 0.25 * self.dt**4, 0, 0, 0.5 * self.dt**3, 0],
                                        [0, 0, 0.25 * self.dt**4, 0, 0, 0.5 * self.dt**3],
                                        [0.5 * self.dt**3, 0, 0, self.dt**2, 0, 0],
                                        [0, 0.5 * self.dt**3, 0, 0, self.dt**2, 0],
                                        [0, 0, 0.5 * self.dt**3, 0, 0, self.dt**2]])

        # Define the measurement noise covariance matrix
        self.R = np.array([[x_std_meas**2, 0, 0],
                           [0, y_std_meas**2, 0],
                           [0, 0, z_std_meas**2]])

    def predict(self):
        # Predict the state
        self.x = np.dot(self.A, self.x) + np.dot(self.B, self.u)

        # Predict the error covariance
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q

        return self.x

    def update(self, z):
        # Compute the Kalman Gain
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))

        # Update the state estimate
        self.x = self.x + np.dot(K, (z - np.dot(self.H, self.x)))

        # Update the error covariance
        self.P = self.P - np.dot(np.dot(K, self.H), self.P)

        return self.x

# Example usage
dt = 0.1
u = np.array([[0], [0], [0]])  # No control input
std_acc = 0.1
x_std_meas = 0.1
y_std_meas = 0.1
z_std_meas = 0.1

kf = KalmanFilter(dt, u, std_acc, x_std_meas, y_std_meas, z_std_meas)

measurements = [np.array([[1], [2], [3]]), np.array([[1.1], [2.1], [3.1]]), np.array([[0.9], [1.9], [2.9]])]

for z in measurements:
    kf.predict()
    state = kf.update(z)
    print("Updated state:\n", state)
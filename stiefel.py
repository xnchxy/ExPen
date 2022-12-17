import numpy as np

from numpy.linalg import svd

class stiefel:
    def __init__(self, n, p) -> None:
        self._n = n
        self._p = p
        self.dim = n*p 



    def Phi(self, M):
        return (M + M.T)/2


    def A(self, X):
        XX = X.T @ X
        return 1.5 * X - X @ (XX /2)


    def JA(self, X, G):
        return G - X @ self.Phi(X.T @ G)


    def JA_exact(self,X, G):
        XX = X.T @ X
        return 1.5 * G - 0.5 * G @ XX - X @ self.Phi(X.T @ G)


    def JC(self, X, Lambda):
        return X @ self.Phi(Lambda)

    
    def C(self, X):
        return X.T @ X - np.eye(self._p)

    def Feas_eval(self, X):
        return np.linalg.norm( self.C(X) , 'fro')

    def Init_point(self, Xinit = None):
        if Xinit is None:
            Xinit = np.random.randn(self._n, self._p)
            
        if np.linalg.norm(Xinit.T @ Xinit - np.eye(self._p), 'fro') > 1e-6:
            Xinit, Rinit = np.linalg.qr(Xinit)
        return Xinit

    def Post_process(self,X):
        UX, SX, VX = svd(X, full_matrices = False)
        return UX @ VX

# Smooth Exact Penalty Functions for Optimization over the Stiefel manifold

## Problem Description

This solver aims to to solve the following optimization problem over the Stiefel manifold,
$$
\begin{aligned}
		\min_{X \in \mathbb{R}^{n\times p}} \quad &f(X)\\
		\text{s.t.} \quad & X^\top X = I_p,
	\end{aligned}
$$
where $I_p$ refers to the $p$-th order identity matrix. We show that the optimization problem over the Stiefel manifold is equivalent to the minimization of the following smooth exact penalty function (ExPen),
$$
h(X) := f\left(X  \left(\frac{3}{2}I_p - \frac{1}{2} X^\top X\right) \right) + \frac{\beta}{4} ||X^\top X - I_p||_F^2,
$$
where $\beta > 0$ is the penalty parameter. Interested readers can refer [our paper](https://arxiv.org/abs/2110.08986) for detailed description on the equivalence.



## Reference

Xiao, Nachuan, and Xin Liu. "Solving optimization problems over the Stiefel manifold by smooth exact penalty function." *arXiv preprint arXiv:2110.08986* (2021).



## Requirements

* scipy
* numpy
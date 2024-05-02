# rayon de courbure pour une courbe 2D avec une abcisse curviligne t

# x(t), y(t)
# dx(t)  : 1st derivative of x(t)
# dy(t)  : 1st derivative of y(t)
# ddx(t) : 2nd derivative of x(t)
# ddy(t) : 2nd derivative of y(t)

R[t]= np.abs(( (dx(t)**2+dy(t)**2) **(3/2) )/(dx(t)*ddy(t) - dy(t)*ddx(t)))

#equivalent à : R = norm(v)**3 / norm(v X a) : où v est la vitesse(dérivée première) et a l'acceleration (derivée seconde)
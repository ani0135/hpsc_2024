! $UWHPSC/codes/fortran/fcn1.f90

program fcn1
    implicit none
    real(kind=8) :: y,z
    real(kind=8), external :: fun

    y = 2.
    z = fun(y)
    print *, "z = ",z
end program fcn1

real(kind=8) function fun(x)
    implicit none
    real(kind=8), intent(in) :: x
    fun = x**2
end function fun


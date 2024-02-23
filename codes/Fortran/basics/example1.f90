
! $UWHPSC/codes/fortran/example1.f90

program example1

    implicit none
    real (kind=8) :: x,y,z ! three real numbers of 8 byte each

    x = 4.d0
    y = 2.d-1
    z = x + y
    print *, "z = ", z

end program example1

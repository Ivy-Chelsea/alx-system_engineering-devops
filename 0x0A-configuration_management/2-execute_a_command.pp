#kills a process named killmenow
exec { 'killmenow':
    path    => ['/usr/bin', '/usr/sbin',],
    command => 'pkill killmenow',
    }

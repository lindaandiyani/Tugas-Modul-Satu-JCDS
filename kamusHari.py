days = {
    'senin' : 'monday', 'selasa' : 'Tuesday','rabu' : 'wednesday',
    'kamis':'Thursday','jumat':'Friday','sabtu':'saturday','minggu':'sunday'
}

hari = list(days)
day = list(days.values())
x = input('ketikan nama hari (ENG/IDN):')

if x.lower() in hari :
    engHari = day[hari.index(x.lower())]
    print('bahasas inggrisnya',x,'adalah',engHari)
else:
    idDay = hari[day.index(x.lower())]
    print('bahasa indonesia',x.lower(),'adalah',idDay)
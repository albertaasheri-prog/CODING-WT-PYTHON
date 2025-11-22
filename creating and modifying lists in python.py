#3-4 guest list
guest_list=['Sandra', 'Joseph', 'Davis']
print(guest_list)
print(guest_list[0], 'you are invited to my dinner')
print(guest_list[1], 'you are invited to my dinner')
print(guest_list[2], 'you are invited to my dinner')

#3-5 chamging the guest list
guest_list.pop(1)
print(guest_list)
guest_list.insert(1, 'ellen')
print(guest_list)
print(guest_list[0], 'you are invited to my dinner')
print(guest_list[1], 'you are invited to my dinner')
print(guest_list[2], 'you are invited to my dinner')

#3-6 more guests
print('dear guests we have foynd a bigger table so we shall be inviting more guests')
guest_list.insert(0, 'lia')
guest_list.insert(1, 'lena')
guest_list.append('tina')
print(guest_list)
print(guest_list[0], 'you are invited to my dinner')
print(guest_list[1], 'you are invited to my dinner')
print(guest_list[2], 'you are invited to my dinner')
print(guest_list[3], 'you are invited to my dinner')
print(guest_list[4], 'you are invited to my dinner')
print(guest_list[5], 'you are invited to my dinner')

#3-8 seeing the world
travel=['maldives', 'cape town', 'paris', 'south korea', 'canada']
print(travel)
travel.sort()
print (travel)
travel.sort(reverse=True)
print(travel)
travel.reverse()
print(travel)
travel.sort()
print(travel)
travel.sort(reverse=True)
print(travel)

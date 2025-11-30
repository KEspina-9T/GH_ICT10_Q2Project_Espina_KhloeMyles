from pyscript import display, document #type:ignore


org1 = {
    'Name of the org':'Atelier Fashion Guild',
    'Description':'The Atelier Fashion Guild is an Organization where students can express their creativity, and identity through fashion.',
    'Meeting time':'1 p.m - 3 p.m',
    'Location': 'Magnus Building, 4th floor, Fashion Workshop',
    'Club Moderator':'Prof. Scarlett Ellsworth',
    'Number of members':'30'
        } # dictionary that contains the info for each information needed
def AFG(e):
    document.getElementById('Orgname').innerHTML = "" #Ensures that you can't repeat it
    display(f'Organization : {org1['Name of the org']}', target='Orgname') # this will display the called variable
    display(f'Description : {org1['Description']}', target='Orgname')
    display(f'Meeting Time : {org1['Meeting time']}', target='Orgname')
    display(f'Location : {org1['Location']}', target='Orgname')
    display(f'Moderator : {org1['Club Moderator']}', target='Orgname')
    display(f'Number of Members : {org1['Number of members']}', target='Orgname')

org2 = {
'Name of the org':'Ivory Debate Union',
'Description':'The Ivory Debate Union is an Organization where students can put to use all they have learned in the English class from previous years. Here they can test their critical thinking skills through debates, researches, etc.',
'Meeting time':'2 p.m - 5 p.m',
'Location': 'Lux Building, 8th Floor, room 802',
'Club Moderator':'Prof. Nicholas Park',
'Number of members':'40'

}
def IDU(e):
    document.getElementById('Orgname').innerHTML = ""
    display(f'Organization : {org2['Name of the org']}', target='Orgname')
    display(f'Description : {org2['Description']}', target='Orgname')
    display(f'Meeting Time : {org2['Meeting time']}', target='Orgname')
    display(f'Location : {org2['Location']}', target='Orgname')
    display(f'Moderator : {org2['Club Moderator']}', target='Orgname')
    display(f'Number of Members : {org2['Number of members']}', target='Orgname')
    





org3=  {
'Name of the org':'Ministry of Sciences',
'Description':'The Ministry of Sciences is an Organization where students can make use of their critical thinking skills in order to conduct science experiments and create research papers and studies for future reference in the Science World.',
'Meeting time':'2 p.m - 6 p.m',
'Location': 'Factum Building, 7th floor, Science Laboratory',
'Club Moderator':'Dr. Adam Carlsen',
'Number of members':'30'
}

def MoS(e):
    document.getElementById('Orgname').innerHTML = ""
    display(f'Organization : {org3['Name of the org']}', target='Orgname')
    display(f'Description : {org3['Description']}', target='Orgname')
    display(f'Meeting Time : {org3['Meeting time']}', target='Orgname')
    display(f'Location : {org3['Location']}', target='Orgname')
    display(f'Moderator : {org3['Club Moderator']}', target='Orgname')
    display(f'Number of Members : {org3['Number of members']}', target='Orgname')
class Solution:
    def reformatDate(self, date: str) -> str:
        temp_list = date.split()
        month_hashmap = {
            'Jan':'01',
            'Feb':'02',
            'Mar':'03',
            'Apr':'04',
            'May':'05',
            'Jun':'06',
            'Jul':'07',
            'Aug':'08',
            'Sep':'09',
            'Oct':'10',
            'Nov':'11',
            'Dec':'12',
        }
        day = temp_list[0][:2] if len(temp_list[0])==4 else '0' + temp_list[0][:1]
        output = temp_list[2] + '-' + month_hashmap[temp_list[1]] + '-'  + day
        return output

class Employee:
    def __init__(self, name, id, type='Работник'):
        self.name = name
        self.id = id
        self.type = type
    def get_info(self):
        return f'{self.type} по имени {self.name} с номером {self.id}'

alena = Employee('Алена', '12345', 'Бухгалтер')
#print(alena.get_info())

class Manager(Employee):
    def __init__(self, name, id, department, type='Менеджер', *args):
        super().__init__(name, id)
        self.type = type
        self.department = department
    def get_info(self):
        return super().get_info() + f' работает в отделе {self.department}'
    def manage_project(self):
        return f'{self.type} {self.name} управляет проектом' 
ilya = Manager('Илья', '666', 'Управление продажами', 'Главный менеджер')   
#print(ilya.get_info())
#print(ilya.manage_project())

class Technican(Employee):
    def __init__(self, name, id, specialization, type='Технический работник', *args):
        super().__init__(name, id)
        self.type = type
        self.specialization = specialization
    def get_info(self):
        return super().get_info() + f' специализируется на задаче {self.specialization}'
    def perform_maintenance(self):
        return f'{self.type} {self.name} занимается техобслуживанием' 
masha = Technican('Мария', '777', 'Техобслужвание сайтов')   
#print(masha.get_info())
#print(masha.perform_maintenance())

class TechManager(Technican, Manager):
    def __init__(self, name, id, specialization, department, type='Технический менеджер'):
        #print(department)
        #Manager.__init__(self, name, id, department)
        #print(department)
        #Technican.__init__(self, name, id, specialization)
        #self.type = type
        super().__init__(self, name, id, specialization, department)
    def get_info(self):
        return Manager().get_info() + f' и специализируется на задаче {self.specialization}'
    def perform_maintenance(self):
        return super().perform_maintenance()
    def manage_project(self):
        return super().manage_project()
    def manage_tech_project(self, project):
        return f'{self.type} {self.name} Возглавляет технический проект {project}'

noname = TechManager('кто-то', '-10', 'системная администрация', 'общение с клиентами', 'Старший технический менеджер')
#print(noname.get_info())
#print(noname.perform_maintenance())
#print(noname.manage_project())
#print(noname.manage_tech_project('расширение колл-центра'))
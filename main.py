'''<--------OS LAB-9--------->
    Groups Members
    => Muhammad Hamza Amir
    => Abdul Rafay Ahmad '''



from ordered_set import OrderedSet
import inspect
from threading import current_thread
import threading
import os
import sys

sys.setrecursionlimit(2000)
n = len(sys.argv)

if n != 2:
    print("<python3> <File name> <Number of Threads>" + " on linux")
    print("<python> <File name> <Number of Threads>" + " on windows")
    sys.exit()
console_args = int(sys.argv[1])



# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.index = None
        self.total_size = 100
        self.id = None
        self.next = None


# Linked List class
class LinkedList:

    def __init__(self):
        self.l_size = 10000
        self.head = None
        self.t_nodes = 100
        self.nodes = 0


    def printList(self):
        temp = self.head
        text = ""
        while (temp):
            text = text+temp.data+"#"+temp.id+"\n"
            temp = temp.next
        return text

    def compute_size(self):
        size_val = 1
        temp = self.head
        while (temp):
            size_val = size_val+1
            temp = temp.next
        return (size_val * 100)

    def insert_node(self, new_data, n_id):

        new_node = Node(new_data)
        new_node.id = n_id
        i = 0

        if (self.nodes <= self.t_nodes):
            if (len(new_data) <= new_node.total_size):

                if self.head is None:
                    new_node.index = i
                    #new_node.size = len(new_data)
                    self.nodes = self.nodes + 1
                    i = i+1
                    self.head = new_node
                    return

                last = self.head

                while (last.next):
                    last = last.next
                    i = i+1

                last.next = new_node
                new_node.index = i+1
                self.nodes = self.nodes + 1
                #new_node.size = len(new_data)
            else:
                self.data_management(new_node, new_data, n_id)
        else:
            print("There no more new sectors available")

    def data_management(self, node, new_data, n_id):
        total_nodes = (len(new_data) // node.total_size) + 1

        for i in range((total_nodes)):
            data_to_add = new_data[i*100:(i+1)*100]
            self.insert_node(data_to_add, n_id)
    # append func

    def add_data(self, new_data, n_id):
        temp = self.head
        while (temp):
            if (temp.id == n_id):
                temp_size = temp.total_size - len(temp.data)
                if ((temp_size > 0)):
                    temp.data = temp.data + new_data[:temp_size]

            temp = temp.next
        if (temp_size < len(new_data)):
            self.data_management(self.head, new_data[temp_size:], n_id)

    def write_to_file_insert_node(self, new_data, n_id):
        temp = self.head
        j = 0
        while (temp):
            if (temp.id == n_id):
                j = j+1
            temp = temp.next
        if (j > 0):
            #print("\ninside j")
            self.turncate(len(new_data), n_id)
            self.write_at_data_OVERWRITE(0, new_data, n_id)
        else:
            #print("\nelse why")
            self.insert_node(new_data, n_id)

    def delete_one_node(self, key):
        # Store head node
        temp = self.head

        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                self.nodes = self.nodes-1
                return

        while(temp is not None):
            if temp.data == key:
                self.nodes = self.nodes-1
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        prev.next = temp.next

        temp = None

    def deleteNode(self, n_id):

        temp = self.head
        prev = None

        while (temp != None and temp.id == n_id):
            self.head = temp.next
            temp = self.head
            self.nodes = self.nodes-1
        while (temp != None):

            while (temp != None and temp.id != n_id):
                prev = temp
                temp = temp.next
                self.nodes = self.nodes-1

            if (temp == None):
                return self.head

            prev.next = temp.next

            temp = prev.next
        self.indices_order()

    def indices_order(self):
        temp = self.head
        i = 0
        while (temp):
            temp.index = i
            i = i+1
            temp = temp.next

    def move_data_ll(self, start, to, size, n_id):
        temp = self.head
        text = ""
        while (temp):
            if (temp.id == n_id):
                text = text + temp.data
            temp = temp.next

        # getting the specific substring from the string
        part_text = text[start:start+size]
        # removing the specific substring from the string
        text = text[0:start:] + text[start+size::]
        # moving the specific substring to particular point in the string
        text = text[0:to] + part_text + text[to:]
        r_text = text
        temp = self.head
        i = 0
        while (temp):
            if (temp.id == n_id):
                data_to_add = text[i*100:(i+1)*100]
                i = i+1
                temp.data = data_to_add
            temp = temp.next
        return r_text

    def write_at_data_noOVERWRITE(self, write_at, text, n_id):
        temp = self.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        self.add_data(text, n_id)
        r_text = self.move_data_ll(len(o_text), write_at, len(text), n_id)
        return r_text

    def write_at_data_OVERWRITE(self, write_at, text, n_id):
        temp = self.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        #part_text = o_text[write_at:write_at+len(text)]
        o_text = o_text[0:write_at:] + o_text[write_at+len(text)::]
        o_text = o_text[0:write_at] + text + o_text[write_at+len(text):]
        r_text = o_text
        temp = self.head
        i = 0
        while (temp):
            if (temp.id == n_id):
                data_to_add = o_text[i*100:(i+1)*100]
                i = i+1
                temp.data = data_to_add
            temp = temp.next
        return r_text

    # read data from start

    def read_file(self, n_id):
        temp = self.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        return o_text

    # read data at a particular point
    def read_file_atpoint(self, n_id, start, size):
        text = self.read_file(n_id)
        part_text = text[start:start+size]
        return part_text

    def turncate(self, maxSize, n_id):
        temp = self.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        part_text = o_text[0:maxSize]
        temp = self.head
        i = 0
        while (temp):
            if (temp.id == n_id):
                data_to_add = part_text[i*100:(i+1)*100]
                i = i+1
                temp.data = data_to_add
            temp = temp.next

        temp = self.head
        del_text = "HASTA_LA_VISTA_BABY"
        while (temp):
            if (temp.id == n_id):
                if (len(temp.data) < 1):
                    temp.data = del_text
                    self.delete_one_node(del_text)
            temp = temp.next

        temp = self.head
        while (temp):
            if (temp.id == n_id):
                self.delete_one_node(del_text)
            temp = temp.next
        return part_text

    def memory_map(self):
        temp = self.head
        total_size = 0
        exlist = []
        while (temp):
            total_size = total_size+len(temp.data)
            print("File Name:", temp.id,
                  " Size of node occupying:", len(temp.data), "Thread : ", current_thread().name)
            exlist.append(temp.id)
            temp = temp.next
        exlist = list(set(exlist))
        print("Total Size occuppied: ", total_size)
        print("Total Size alloted: ", (self.compute_size()-100))
        print("Total Size: ", self.l_size)
        print("Total Sectors: ", self.t_nodes)
        print("Available Sectors: ", (self.t_nodes -
                                      self.nodes))
        print("Available sector size on disk: ",
              (100+self.l_size-self.compute_size()))
        print("Available size orignally: ",
              (self.l_size-(total_size)))

    def get_data(self, text):
        for line in text.splitlines():
            a_l = line.split("#")
            self.insert_node(a_l[0], a_l[1])
        self.indices_order()


class fileHandling:

    def __init__(self):
        self.file_name = ""
        self.llist = LinkedList()

    def Create(self, *args):
        args = list(args)
        fname = args[0]
        self.file_name = fname+".txt"
        try:
            self.file = open("output"+current_thread().name+".txt", "a+")
            self.file.write("#"+fname)
            self.file.close()
        except:
            pass
        print("File is Created "+"by Thread-"+current_thread().name+"\n")

    def Delete(self, *args):
        args = list(args)
        fname = args[0]
        self.file_name = ""
        try:
            self.file = open("output"+current_thread().name+".txt", "w+")

            self.llist.deleteNode(fname)
            text = self.llist.printList()
            self.file.write(text)
            self.file.close()
            print("File is Deleted "+"by Thread-"+current_thread().name+"\n")
        except:
            pass

    def Open(self, *args):
        args = list(args)
        fname = args[0]
        mode = args[1]
        self.file_name = fname
        print("File is Opened "+"by Thread-"+current_thread().name+"\n")
        # return f

    def Close(self, *args):
        args = list(args)
        fname = args[0]
        self.file_name = fname
        print("File is Closed "+"by Thread-"+current_thread().name+"\n")

    # write_at_first_time
    def write_to_file(self, *args):
        try:
            args = list(args)
            fname = args[0]
            text = args[1]
            
            self.file = open("output"+current_thread().name+".txt", "w+")
            v = self.file
            self.llist.write_to_file_insert_node(text, fname)
            text = self.llist.printList()
            v.write(text)
            self.file.close()
            
            print("Text has been written " +
                  "by Thread-"+current_thread().name+"\n")
        except:
            pass

    def write_at_OVERWRITE(self, fname, write_at, text):
        try:
         
            self.file = open("output"+current_thread().name+".txt", "w+")
            v = self.file
            s = text
            p = write_at
            self.llist.write_at_data_OVERWRITE(int(p), s, fname)
            t = self.llist.printList()
            v.write(t)
            self.file.close()
          
            print("Text has been written " +
                  "by Thread-"+current_thread().name+"\n")
        except:
            pass

    def write_at_noOVERWRITE(self, fname, write_at, text):
        try:
            
            self.file = open("output"+current_thread().name+".txt", "w+")
            v = self.file
            s = text
            p = write_at
            self.llist.write_at_data_noOVERWRITE(int(p), s, fname)
            t = self.llist.printList()
            v.write(t)
            self.file.close()
            
            print("Text has been written " +
                  "by Thread-"+current_thread().name+"\n")
        except:
            pass

    def Write_to_File_over(self, *args):
        args = list(args)
        fname = args[0]
        write_at = args[1]
        text = args[2]
        print("Do you want to Overwrite? If Yes then write 1 ")
        cond = input("Entre: ")
        if str(cond) == "1":
            self.write_at_OVERWRITE(fname, int(write_at), text)
        else:
            self.write_at_noOVERWRITE(fname, int(write_at), text)

    def Read_From_File(self, *args):
        args = list(args)
        fname = args[0]
        t = self.llist.read_file(fname)
        print(t)

    #Write in End

    def appendFile(self, *args):
        try:
            args = list(args)
            fname = args[0]
            text = args[1]
            
            self.file = open("output"+current_thread().name+".txt", "w+")
            v = self.file
            s = text
            self.llist.add_data(s, fname)
            t = self.llist.printList()
            v.write(t)
            self.file.close()
          
            print("Text Has been Appended " +
                  "by Thread-"+current_thread().name+"\n")
        except:
            pass

    def Move_within_file(self, *args):
        try:
            args = list(args)
            fname = args[0]
            start = args[1]
            size = args[2]
            target = args[3]
            
            self.file = open("output"+current_thread().name+".txt", "w+")
            v = self.file
            p = start
            s = target
            size = size
            self.llist.move_data_ll(int(p), int(s), int(size), fname)
            t = self.llist.printList()
            v.write(t)
            self.file.close()
     
            print("Text Has been Moved "+"by Thread-"+current_thread().name+"\n")
        except:
            pass

    def read_from_file_at(self, *args):
        try:
            args = list(args)
            fname = args[0]
            start = args[1]
            size = args[2]
            
            self.file = open("output"+current_thread().name+".txt", "w+")
            v = self.file.name
            p = start
            size = size
            try:
                text = self.llist.read_file_atpoint(
                    fname, int(p), int(size))
                print(text)
                self.file.close()
               
            except:
                self.file.close()
                
                print("")
        except:
            pass

    def truncate(self, *args):
        v = self.file
        name = v.name
        args = list(args)
        fname = args[0]
        maxSize = args[1]
        try:
           
            self.file = open("output"+current_thread().name+".txt", "w+")
            self.llist.turncate(int(maxSize),  fname)
            v = self.file
            t = self.llist.printList()
            self.file.write(t)
            self.file.close()
           
            print("File has been Truncated " +
                  "by Thread-"+current_thread().name+"\n")
        except:
            self.file = open("output"+current_thread().name+".txt", "w+")
            self.llist.turncate(int(maxSize),  fname)
            t = self.llist.printList()
            v = self.file
            self.file.write(t)
            self.file.close()
            
            print("File has been Truncated " +
                  "by Thread-"+current_thread().name+"\n")

    def show_memory_map(self):
        try:
            self.llist.memory_map()
        except:
            pass

    def system_exit(self):
        self.file.close()


class threading_class:
    def __init__(self, thread_name_obj):
        self.file_hand = fileHandling()
        self.threading_list = []
        self.jt = 0
        
        self.t = threading.Thread(target=self.read_input_file, args=[str(thread_name_obj)],daemon=True)
        self.t.name = str(thread_name_obj)

    def thread_start(self):
        self.t.start()
    
    def thread_join(self):
        self.t.join()

    def read_input_file(self, thread_name):
        file = open("input"+thread_name+".txt")
        lines_list = []
        for line in file:
            lines_list.append(line.strip())
        file.close()

        for i in range(len(lines_list)):
            data_line = lines_list[i]
            list_data = data_line.split("#")
            self.execute_program(list_data)
        self.file_hand.system_exit()

        

    def execute_program(self, data_list):
        functions_of_file_handling_class = inspect.getmembers(
            fileHandling, predicate=inspect.isfunction)
        function_to_perform = ""
        for i in range(len(functions_of_file_handling_class)):
            if (functions_of_file_handling_class[i][0].lower() == data_list[0].lower()):
                function_to_perform = functions_of_file_handling_class[i][0]

        pt = []
        for j in range(len(data_list)-1):
            pt.append(data_list[j+1])

        self.call_func_dynamically(function_to_perform, pt)

    def call_func_dynamically(self, name, list_ge):
        getattr(self.file_hand, name)(*list_ge)

    def dat_file_sync(self):
        p = ""  # variable for dat file exclusive
        ex_p = ""
        files_lists_data = []
        t_f_data = ""  # just a useless variable
        updated_file_lists_data_final = []
        updated_file_lists_data_1_0_inner = []
        set_of_data = []
        updated_file_lists_data_1_0_outer = []
        try:
            self.file = open("sample.dat", "r+")
            p = self.file.read()
            self.file.close()
        except:
            pass

        self.file_hand.llist.get_data(p)
        for i in range(int(sys.argv[1])):
            inp_file = open("output"+str(i)+".txt", "r+")
            data = inp_file.read()
            files_lists_data.append(data)
            t_f_data = t_f_data + data
            inp_file.close()
            

        for k in range(len(files_lists_data)):
            ex_list = []
            for j in files_lists_data[k].splitlines():

                updated_file_lists_data_1_0_inner.append(j)
                ex_list.append(j)
            updated_file_lists_data_1_0_outer.append(
                updated_file_lists_data_1_0_inner)

        seen = set()
        set_of_data = [x for x in updated_file_lists_data_1_0_inner if not (
            x in seen or seen.add(x))]
        

        ex_text = []
        for i in range(len(set_of_data)):
            ex_ = set_of_data[i].split("#")
            ex_text.append(ex_[1])

        seen = set()
        ex_set_file_name = [x for x in ex_text if not (
            x in seen or seen.add(x))]

        

        for i in range(len(ex_set_file_name)):
            tes = ""
            for j in range(len(set_of_data)):
                ex_ = set_of_data[j].split('#')
                if ex_set_file_name[i] == ex_[1]:
                    tes = tes + ex_[0]
            tes = tes + "#" + ex_set_file_name[i]
            updated_file_lists_data_final.append(tes)

       

        

        for k in range(len(updated_file_lists_data_final)):
            in_p = updated_file_lists_data_final[k]+"\n"
            ex_p = ex_p + in_p
        

        dat_struc = LinkedList()
        dat_struc.get_data(ex_p)
        final_updated_data = dat_struc.printList()
        dat_file = open("sample.dat", "w+")
        dat_file.write(final_updated_data)
        dat_file.close()
        return dat_struc


dat_st = None
if n == 2:
    for i in range(int(sys.argv[1])):
        obj = threading_class(i)
        obj.thread_start()
        obj.thread_join()
        #dat_st = obj.dat_file_sync()
    dat_st = obj.dat_file_sync()
    dat_st.memory_map()
    
else :
    print("<python3> <File name> <Number of Threads>" + "on linux")
    print("<python> <File name> <Number of Threads>" + "on windows")

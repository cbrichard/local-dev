Vagrant.configure("2") do |config|
  #config.vm.provision "chef_solo" do |chef|
  #  chef.cookbooks_path = "chef-repo/cookbooks"
  #  chef.roles_path = "chef-repo/roles"
  #  chef.data_bags_path = "chef-repo/data_bags"
  #  chef.add_role("base")
  #end
  config.vm.define "alpha" do |alpha|
    alpha.vm.box = "ubuntu/xenial64"
    alpha.vm.hostname = 'alpha'
    alpha.vm.box_url = "ubuntu/xenial64"

    alpha.vm.network :private_network, ip: "192.168.56.101"

    alpha.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "alpha"]
    end
  end

  config.vm.define "tango" do |tango|
    tango.vm.box = "ubuntu/xenial64"
    tango.vm.hostname = 'tango'
    tango.vm.box_url = "ubuntu/xenial64"

    tango.vm.network :private_network, ip: "192.168.56.102"

    tango.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "tango"]
    end
  end
  config.vm.define "foxtrot" do |foxtrot|
    foxtrot.vm.box = "ubuntu/xenial64"
    foxtrot.vm.hostname = 'foxtrot'
    foxtrot.vm.box_url = "ubuntu/xenial64"

    foxtrot.vm.network :private_network, ip: "192.168.56.103"

    foxtrot.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 1024]
      v.customize ["modifyvm", :id, "--name", "foxtrot"]
    end
  end
end

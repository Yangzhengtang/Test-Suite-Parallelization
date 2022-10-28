import os
import glob
import urllib
import json
import urllib.request
import time

projects = ["activiti/activiti",
            "alibaba/fastjson",
            "apache/hadoop",
            "apache/jackrabbit-oak",
            "apache/struts",
            "crawlscript/webcollector",
            "doanduyhai/achilles",
            "dropwizard/dropwizard",
            "elasticjob/elastic-job-lite",
            "google/jimfs",
            "jfree/jfreechart",
            "jodaorg/joda-time",
            "kevinsawicki/http-request",
            "knightliao/disconf",
            "looly/hutool",
            "orbit/orbit",
            "oryxproject/oryx",
            "querydsl/querydsl",
            "spotify/helios",
            "spring-projects/spring-boot",
            "square/otto",
            "square/retrofit",
            "tootallnate/java-websocket",
            "undertow-io/undertow",
            "wildfly/wildfly",
            "wro4j/wro4j"]

def get_most_star_repo():
    query = "https://api.github.com/search/repositories?q=language:java+stars:%3E=100+pushed:%3E=2022+mvn%20in:readme&sort=stars&per_page=100"
    all_projects = []
    for i in range(1, 6):
        time.sleep(5)
        with urllib.request.urlopen(query + "&page={}".format(i)) as url:
            s = url.read().decode('utf8')
            page = json.loads(s)
            projects = [item['full_name'] for item in page['items'] if item['visibility']=='public']
            all_projects = all_projects + projects
    print(len(all_projects))
    print(all_projects)
    return all_projects

def get_loc(projects):
    for project in projects:
        name = project.split("/")[1]
        os.system("git clone https://github.com/{} {}".format(project, name))
        readme_paths = ["{}/{}".format(name, "README")
        , "{}/{}".format(name, "readme")
        , "{}/{}".format(name, "README.md")
        , "{}/{}".format(name, "readme.md")
        , "{}/{}".format(name, "Readme")]
        is_mvn = True
        for readme in readme_paths:
            if not os.path.isfile(readme):
                continue
            with open(readme, 'r') as f:
                text = f.read()
                if "mvn" not in text:
                    is_mvn = False
        if not is_mvn:
            continue
        java_files = []
        java_files = glob.glob(name+ '/**/*.java', recursive=True)
        total_cnt = 0
        for java_file in java_files:
            num_lines = sum(1 for line in open(java_file))
            total_cnt += num_lines
            # print("{}-{}".format(java_file, num_lines))
        with open("LOC.txt", "a") as loc_file:
            loc_file.write("{} - {}\n".format(project, total_cnt))


# get_most_star_repo()
projects = get_most_star_repo()
get_loc(projects)

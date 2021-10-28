# Notes
Refering to [caninedc.org manifest](https://github.com/uc-cdis/cdis-manifest/blob/master/caninedc.org/manifest.json)


## versions section changes
Changing it to use docker images from [docker-compose.yml](https://github.com/NIEHS/compose-services/blob/master/docker-compose.yml) in NIEHS/compose-services.  
For production we can later use AWS ECR if images need tweaking

**Removed:** need to review services before adding to deployment
* [hatchery](https://github.com/uc-cdis/hatchery)
* [wts](https://github.com/uc-cdis/workspace-token-service)
* [manifestservice](https://github.com/uc-cdis/manifestservice)
* [sower](https://github.com/uc-cdis/sower)
* [ssjdispatcher](https://github.com/uc-cdis/ssjdispatcher)
* [ambassador](https://github.com/uc-cdis/cloud-automation/tree/master/kube/services/ambassador)

## ssjdispather section
ignored as image is not included in version section

## sower section
ignored as image is not included in version section

## global
ToDo:
* add AWS revproxy_arn
* add dictionary url, as S3 bucket http link  
* add user yaml, as S3 path

## canary section 
as it is

## guppy section
copied from gitlab NIEHS-Gen3 [guppy_config.json](https://gitlab.niehs.nih.gov/conwaymc/niehs-gen3/-/blob/master/data-model-ods/ver-1.1/if_and_etl_customizations/guppy_config.json) 
